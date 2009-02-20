%define name mono-nat
%define version 1.0
%define release %mkrel 1

Summary: Network Address Translation library for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.monsoon-project.org/jaws/data/files/%{name}-%{version}.tar.gz
License: MIT
Group: System/Libraries
Url:  http://www.monsoon-project.org/jaws/index.php?
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildArch: noarch

%description
This is a .NET Library for automatic network address translation.

%prep
%setup -q

%build
./configure --prefix=%_prefix
make

%install
rm -rf %{buildroot}
%makeinstall_std linuxpkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_prefix/lib/mono-nat
%_datadir/pkgconfig/mono.nat.pc
